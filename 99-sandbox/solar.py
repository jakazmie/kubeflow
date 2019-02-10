from __future__ import absolute_import

import argparse
import logging
import re

from past.builtins import unicode

import apache_beam 
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from datetime import datetime


class SortReadings(apache_beam.DoFn):
    def process(self, element):
        
        element[1].sort()
        sorted_readings = [reading[1] for reading in element[1]]
        
        # TODO: Pad and remove short sequences
        
        return (element[0], sorted_readings)
        

options = PipelineOptions()

with apache_beam.Pipeline(options=options) as p:

    raw_readings = (
        p | 
        apache_beam.io.ReadFromText('data/solar.csv', skip_header_lines=1) |
        apache_beam.Map(lambda x: x.replace(' ', ',').split(','))
    )
    
    current_by_day = (
        raw_readings |
        apache_beam.Map(lambda x: (x[0], (str(x[1]), float(x[2])))) |
        "Current By Day" >> apache_beam.GroupByKey() |
        apache_beam.ParDo(SortReadings())
    )
    
    total_by_day = (
        raw_readings |
        apache_beam.Map(lambda x: (x[0], float(x[3]))) |
        "Total By Day" >> apache_beam.GroupByKey() 
    )
    
    processed_readings = (
        current_by_day
    )
  
    (
        processed_readings | 
        "Final write" >> apache_beam.io.WriteToText('res1.txt')
    )
    

print(p.run())


    daily_readings = (
        raw_readings |
        apache_beam.Map(lambda x: (x['date'], (x['date_time'], x['current']))) |
        "Grouping reading" >> apache_beam.GroupByKey() 

    )


    raw_readings = (
        p | 
        apache_beam.io.ReadFromText('data/solar.csv', skip_header_lines=1) |
        apache_beam.ParDo(Split()) 
    )

    

    daily_totals = (
        raw_readings |
        apache_beam.Map(lambda x: (x['date'], x['total'])) |
        "Grouping totals" >> apache_beam.GroupByKey() |
        apache_beam.Map(lambda x: (x[0], max(x[1]))) 
        
    )
  



    daily_readings = (
        raw_readings |
        apache_beam.Map(lambda x: (x['date'], x['current'])) |
        "Grouping reading" >> apache_beam.GroupByKey() 

    )


    to_be_joined = (
        {
            'daily_readings': daily_readings,
            'daily_totals': daily_totals
        } |
        apache_beam.CoGroupByKey() |
        "Final write" >> apache_beam.io.WriteToText('res.txt')
    )
