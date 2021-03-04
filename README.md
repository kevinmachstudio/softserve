name: Cron

# Run this workflow every 5 minutes
on:
  schedule:
    - cron:  '*/5 * * * *'

jobs:
  # Set the job key. The key is displayed as the job name
  # when a job name is not provided
  diamond:
    # Name the Job
    name: Curl serverless function
    # Set the type of machine to run on
    runs-on: ubuntu-latest

    steps:
      - name: curl
        uses: wei/curl@v1
        with:
          args: -X GET https://softserve.vercel.app/api/index 

# This serverless function runs on Vercel and is called via a cron job on console.cron-job.org/jobs
