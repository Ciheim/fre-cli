"""
frepp.py, a replacement for the frepp bash script located at:
https://gitlab.gfdl.noaa.gov/fre2/system-settings/-/blob/main/bin/frepp
Author: Carolyn.Whitlock
"""

# add relative path import to rest of pp tools
# add command-line args using same format as fre.py
# include arg for pp start / stop
# test yaml path
# error handling

import os
#import time
import click

# Import from the local packages
from fre.pp.checkout_script import checkout_template
from fre.pp.configure_script_yaml import yaml_info
from fre.pp.install_script import install_subtool
from fre.pp.run_script import pp_run_subtool
from fre.pp.trigger_script import trigger
from fre.pp.status_script import status_subtool

def run_all_fre_pp_steps(experiment, platform, target, config_file, branch=None, time=None):
    '''
    Wrapper script for calling a FRE2 pp experiment with the canopy-style
    infrastructure and fre-cli
    '''
    print('(run_all_fre_pp_steps) config_file path resolving...')
    config_file = os.path.abspath(config_file)
    print(f'            config_file={config_file}')

    print('(run_all_fre_pp_steps) calling checkout_template')
    checkout_template(experiment, platform, target, branch)

    print('(run_all_fre_pp_steps) calling yaml_info')
    yaml_info(config_file, experiment, platform, target)

    print('(run_all_fre_pp_steps) calling install_subtool')
    install_subtool(experiment, platform, target)

    print('(run_all_fre_pp_steps) calling pp_run_subtool')
    pp_run_subtool(experiment, platform, target)

    if time is not None:
        print('(run_all_fre_pp_steps) calling trigger')
        trigger(experiment, platform, target, time)

    print('(run_all_fre_pp_steps) calling status_subtool')
    status_subtool(experiment, platform, target)

    print('(run_all_fre_pp_steps) done.')


@click.command()
def _run_all_fre_pp_steps(experiment, platform, target, config_file, branch, time):
    '''
    click entry point for run_all_fre_pp_steps.
    '''
    return run_all_fre_pp_steps(experiment, platform, target, config_file, branch, time)

if __name__ == '__main__':
    run_all_fre_pp_steps()