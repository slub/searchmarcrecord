#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

from pymarc import MARCReader


def run():
    parser = argparse.ArgumentParser(prog='searchmarcrecord',
                                     description='searches a single MARC record via a given id (controlfield 001) in a given (binary) MARC records file and writes it into a single (binary) MARC file',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    optional_arguments = parser._action_groups.pop()

    required_arguments = parser.add_argument_group('required arguments')
    required_arguments.add_argument('-id', type=str, help='the record id', required=True)
    required_arguments.add_argument('-input-file', type=str, help='the input MARC file (with multiple records)',
                                    required=True, dest='input_file')
    required_arguments.add_argument('-output-file', type=str, help='the output MARC file (with one found record)',
                                    required=True, dest='output_file')

    optional_arguments.add_argument('-continue-search-after-first-hit', action="store_true",
                                    help='continues search after first hit, i.e., also determines whether multiple records for the given id occur in the input MARC records file',
                                    dest='continue_search_after_first_hit')

    parser._action_groups.append(optional_arguments)

    args = parser.parse_args()

    marc_record_id = args.id
    input_file = args.input_file
    output_file = args.output_file
    found_counter = 0

    with open(input_file, 'rb') as marc_records_file:
        reader = MARCReader(marc_records_file)
        for record in reader:
            record_id_list = record.get_fields('001')
            if record_id_list is not None and len(record_id_list) == 1:
                record_id = record_id_list[0].data
                if record_id == marc_record_id:
                    marc_record_file = open(output_file, 'wb')
                    marc_record_file.write(record.as_marc())
                    marc_record_file.close()
                    found_counter += 1
                    if not args.continue_search_after_first_hit:
                        break

    search_result_appendix = ''

    if not args.continue_search_after_first_hit:
        search_result_appendix = ' (stopped search after first hit)'

    print('found {:d} MARC record(s) for id {:s}{:s}'.format(found_counter, marc_record_id, search_result_appendix))


if __name__ == "__main__":
    run()
