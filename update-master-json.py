import commands, sys, json, os, shutil

""" A tool for generating a master_config.json file from 
    production_masters.json for a specific master 
    
"""

if len(sys.argv) == 3:
    all_masters_json = sys.argv[1]
    hostname = commands.getoutput('hostname')
    cwd = os.getcwd()
    if os.path.exists(all_masters_json):
        masters = json.load(open(all_masters_json))
        found = False
        for master in masters:
            if master['hostname'] == hostname and master['basedir'] == cwd and master['enabled']:
                found = True
                tmp = json.dumps(master, indent=2, sort_keys=True)
                if len(tmp) > 0:
                    print "writing new master_config.json file to %s" % sys.argv[2]
                    f = open(sys.argv[2], 'w')
                    f.write(tmp)
                    f.close()
                else:
                    print "no changes to master_config.json"
        if not found:
            print 'master not found in %s' % sys.argv[1]
            sys.exit(1)
    else:
        print '%s does not exist - please check path and try again' % sys.argv[1]
        sys.exit(1)
else:
    sys.stderr.write('Usage: %s production-masters.json master_config.json' % sys.argv[0])
    sys.exit(1)
