#!/usr/bin/env python3
import argparse
import textwrap
import os
import logger
import helper

def _quit():
    TERM_FLAGS = termios.tcgetattr(sys.stdin.fileno())
    termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, TERM_FLAGS)

def _init(project_name, output_dir):
    # atexit.register(_quit)
    project_dir = os.path.join(output_dir, project_name)
    #create proj dir
    if os.path.isdir(project_dir):
        #prompt if they wanna overwrite
        v.warn("Directory " + project_dir + " exists!")
        if not helper.query_yes_no("Would you like to write to this directory?"):
            raise FileExistsError
    else:
        #create project dir
        pass
        v.log("Creating directory " + project_dir)
        os.makedirs(project_dir, exist_ok=True)

    report_dir = os.path.join(project_dir, "report")
    scans_dir = os.path.join(project_dir, "scans")
    logs_dir = os.path.join(project_dir, "logs")
    # create these sub directories

    # Confirm this directory exists;

    return 0

    if "username_wordlist" in service_scans_config:
        if isinstance(service_scans_config["username_wordlist"], str):
            username_wordlist = service_scans_config["username_wordlist"]

    if "password_wordlist" in service_scans_config:
        if isinstance(service_scans_config["password_wordlist"], str):
            password_wordlist = service_scans_config["password_wordlist"]


def main():
    """Default Values"""
    output_dir = os.getcwd()
    global v 
    parser = argparse.ArgumentParser(description='AutoRecon but ZeroTouch',  formatter_class=argparse.RawTextHelpFormatter)
    """Positional Arguments"""
    parser.add_argument('project_name', action='store', type=str, help='The name for the project')
    parser.add_argument('target', action='store',nargs='*', type=str, help='the target IP(s), range(s), CIDR(s), hostname(s), FQDN(S), or file containing a list of targets (nmap\'s -iL option)')
    parser.add_argument('-t','--target_file', action='store', help='file')
    parser.add_argument('-ct', '--concurrent-targets', action='store', metavar='<number>', type=int, default=5, help='The maximum number of target hosts to scan concurrently. Default: %(default)s')
    parser.add_argument('-cs', '--concurrent-scans', action='store', metavar='<number>', type=int, default=10, help='The maximum number of scans to perform per target host. Default: %(default)s')
    """Optional Arguments"""
    # parser.add_argument('-i','--interactive', action='store_true', default=False, help='Interactive mode')
    # parser.add_argument('-t', '--target', action='store',nargs='*', type=str, help='the target IP(s), range(s), CIDR(s), hostname(s), FQDN(S), or file containing a list of targets (nmap\'s -iL option)')
    # parser.add_argument('-p','--project_name', action='store', type=str, help='The name for the project')
    parser.add_argument('-o','--output', action='store', default=output_dir, help='the output directory for the results.\nDefault: Current Working Directory (%(default)s)')
       
    parser.add_argument('--config', action='store', help='Config file')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Enable verbose output. Repeat for more verbosity.')
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='Enable debug output.')
    parser.add_argument('--no-daemon', action='store_true', default=False, help='Do not daemonize the scanning threads.' )
    #take in arguements
    
    args = parser.parse_args()
    v = logger.Logger(args.debug, args.verbose)
    if args.concurrent_targets <= 0:
        error('Argument -ch/--concurrent-targets: must be at least 1.')
        errors = True

    concurrent_scans = args.concurrent_scans

    if concurrent_scans <= 0:
        error('Argument -ct/--concurrent-scans: must be at least 1.')
        errors = True

    # check for target_file
    if args.target_file:
        raise NotImplementedError
    if args.output:
        output_dir = args.output

    #launch init function, init will prepare directory 
    #create output directories
    print(args)
    _init(args.project_name, output_dir)
    #target objects (with fun stuff)

    #explode targets into objects




    #get the scans and their inputs ready
    #daemonize the process
    #in daemon, make each scan its own thread
    #launch scans via system calls(blocking state)
    #multi-thread it in
    #after the system call is done, send an email with the output? if possible?
    # stdout and stderr might need to be redirected to other files
    #nmap first, let the nmap discover ports,
    # we need to prepare testssl, nikto, gobutser????, wpscan maybe?, other web sstuff
    # subdomain with dns
    # recon-ng possible?

    #first it will scan and port knock (nmap)
    #concurrently, dnssublister will also work in the background
    #concurrently, recon-ng will work

    #phase 1, recon the target ips and figure out what services
    #phase 2, gather all known services and perform extra enumeration

    # verify args
    # verify input file is correct
    # verify bin paths, if no verified then error
    # read targets from input file
    # create target objects
    # create directories

    #daemonize

    #domain sublister on detected domains
    #...
    #if resolvable to an Ip address, look it up in the targets dictionary by IP. If not in target dic, add new target object
    #now for the port scanning
    #for each target, do
    # common ports (--top-ports 10 )
    # top2k(except commonports) 
    # all_tcp
    # all_udp
    # we do this only to discover open ports!
    # https://xael.org/pages/python-nmap-en.html

    # we shoudl use the async method. 
    # in the callback, we should append that information to our targets 


    #goal here is nmap to get all the open ports
    # now for each host,
        #run a enuemration scan for each port
    

    # how do we optimize this??
    # how do we handle getting blcoked?

    # during all this, logging is piped to a log files
    # sendmail(1) for each phase?



if __name__ == '__main__':
    main()
