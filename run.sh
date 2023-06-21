#!/bin/bash
echo ">>-- API Started --<<" 
uvicorn --workers ${NUM_WORKERS} --host 0.0.0.0 scripts.app:app
