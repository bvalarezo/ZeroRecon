#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description='AutoRecon but ZeroTouch')
    parser.add_argument('target' action='store', nargs=*, type=str, help='the target IP(s), range(s), CIDR(s), hostname(s), FQDN(S), or file containing a list of targets (nmap\'s -iL option)')
    parser.add_argument('-I','--interactive', action='store_true', default=False, help='Interactive mode')
    parser.add_argument('')
    #take in arguements
    #launch init function, init will prepare directory 
    #should I hvae interactive mode?
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


if __name__ == '__main__':
    main()
