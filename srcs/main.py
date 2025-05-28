import os
import sys
import argparse

def main():
    # Configure argument parser
    parser = argparse.ArgumentParser(
        description = "Automatically tailor your resume for specific job description",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('job_description')
    parser.add_argument('base_resume')

    args = parser.parse_args()
    
    # Validate input files
    for path in [args.job_description, args.base_resume]:
        if not os.path.exists(path):
            sys.exit(f"Error: File not found - {path}")
        if not os.access(path, os.R_OK):
            sys.exit(f"Error: Cannot read file - {path}")

    # Extract text from job desc
    try:
        print("Processing job description...")
        job_text = open(args.job_description).read()
#def main():
#    if len(sys.argv) == 3:
 #       job_pdf_file = sys.argv[1]
  #      base_cv = sys.argv[2]        
   #     job_elements = job_parser(job_pdf_file)
    #    new_cv = cv_tailor(job_elements, base_cv)
     #   return new_cv
    #return (print("Invalid argument count, include job description pdf file as argv[1]"))

if __name__ == '__main__':
    main()
