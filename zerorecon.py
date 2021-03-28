#!/usr/bin/env python3
import argparse
import textwrap
import os

def _quit():
    TERM_FLAGS = termios.tcgetattr(sys.stdin.fileno())
    termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, TERM_FLAGS)

def _init(project_name, output_dir):
    # global port_scan_profiles_config
    # global service_scans_config
    # global global_patterns

    atexit.register(_quit)
    appname = "ZeroRecon"
    project_dir = os.path.join(os.path.dirname(output_dir), project_name)
    #create proj dir
    if os.path.exists(project_dir):
        #project exits? warning
        #prompt if user would like to overwrite this directroy?
    else:
        #create project dir
        os.makedirs(project_dir, exist_ok=True)

    report_dir = os.path.join(project_dir, "report")
    scans_dir = os.path.join(project_dir, "scans")
    logs_dir = os.path.join(project_dir, "logs")


    # Confirm this directory exists;
    if not os.path.exists(config_dir):
        raise EOFError
    return 0


    with open(port_scan_profiles_config_file, "r") as p:
        try:
            port_scan_profiles_config = toml.load(p)

            if len(port_scan_profiles_config) == 0:
                fail(
                    "There do not appear to be any port scan profiles configured in the {port_scan_profiles_config_file} config file."
                )

        except toml.decoder.TomlDecodeError as e:
            fail(
                "Error: Couldn't parse {port_scan_profiles_config_file} config file. Check syntax and duplicate tags."
            )

    with open(service_scans_config_file, "r") as c:
        try:
            service_scans_config = toml.load(c)
        except toml.decoder.TomlDecodeError as e:
            fail(
                "Error: Couldn't parse service-scans.toml config file. Check syntax and duplicate tags."
            )

    with open(global_patterns_config_file, "r") as p:
        try:
            global_patterns = toml.load(p)
            if "pattern" in global_patterns:
                global_patterns = global_patterns["pattern"]
            else:
                global_patterns = []
        except toml.decoder.TomlDecodeError as e:
            fail(
                "Error: Couldn't parse global-patterns.toml config file. Check syntax and duplicate tags."
            )

    if "username_wordlist" in service_scans_config:
        if isinstance(service_scans_config["username_wordlist"], str):
            username_wordlist = service_scans_config["username_wordlist"]

    if "password_wordlist" in service_scans_config:
        if isinstance(service_scans_config["password_wordlist"], str):
            password_wordlist = service_scans_config["password_wordlist"]


def main():
    """Default Values"""
    output_dir = os.getcwd()

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
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Enable verbose output. Repeat for more verbosity.')
    parser.add_argument('--no-daemon', action='store_true', default=False, help='Do not daemonize the scanning threads.' )
    #take in arguements
    args = parser.parse_args()

    if args.concurrent_targets <= 0:
        error('Argument -ch/--concurrent-targets: must be at least 1.')
        errors = True

    concurrent_scans = args.concurrent_scans

    if concurrent_scans <= 0:
        error('Argument -ct/--concurrent-scans: must be at least 1.')
        errors = True

    # check for target_file
    if 0 < len(args.target_file):
        raise NotImplementedError

    #launch init function, init will prepare directory 
    print(args)
    #target objects (with fun stuff)
    #create output directories

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
