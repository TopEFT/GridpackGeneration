#! /bin/bash

# HTCondor python bindings are lost after cmsenv/scram
# unless PYTHONPATH is set including its location
# Workaround: Include original location in the path
# if not there already.
# EDIT: The following line is from a newer genproductions commit than we're currently on, but is necessary to run (see https://hypernews.cern.ch/HyperNews/CMS/get/generators/5068/3/1.html)
PYTHON_BINDINGS="$(python -c 'import htcondor; import os; print os.path.dirname(htcondor.__path__[0])' 2>/dev/null)"
if [ -z "$PYTHON_BINDINGS" ]; then
    echo "Error: Could not find htcondor python binding (htcondor.so), please include the directory in PYTHONPATH."
    exit 1
else
  if [ -n "$PYTHONPATH" ]; then
      case ":$PYTHONPATH:" in
        *:$PYTHON_BINDINGS:*) :
        ;;
        *) export PYTHONPATH="$PYTHON_BINDINGS:$PYTHONPATH"
        ;;
      esac
  else
      export PYTHONPATH="$PYTHON_BINDINGS"
  fi
  export PYTHON_BINDINGS="$PYTHON_BINDINGS"
fi
