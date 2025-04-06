# MIT 18.06 Linear Algebra, Spring 2005

This repository provides scripts, Korean translations, and SRT subtitle files for MIT's renowned linear algebra course "18.06 Linear Algebra, Spring 2005".

## Project Overview

Professor Gilbert Strang's linear algebra course is one of the most popular mathematics courses worldwide. This project aims to:

1. Preserve the original English scripts provided by YouTube
2. Create Korean translations using GPT and Claude
3. Generate SRT subtitle files based on the translated content

Sections in the English scripts are marked with markdown `#` headers to improve readability.

## Repository Structure

```
.
├── README.md
├── README.en.md          # English version README
├── scripts
│   ├── original          # Original English scripts
│   │   ├── lec01.txt
│   │   ├── lec02.txt
│   │   └── ...
│   └── translated        # Korean translated scripts
│       ├── lec01.txt
│       ├── lec02.txt
│       └── ...
├── srt
│   ├── en                # English SRT subtitle files
│   │   ├── lec01.srt
│   │   ├── lec02.srt
│   │   └── ...
│   └── ko                # Korean SRT subtitle files
│       ├── lec01.srt
│       ├── lec02.srt
│       └── ...
└── tools                 # Conversion and processing tools
    ├── txt_to_srt.py     # Text script to SRT file converter
    └── ...
```

## Translation Process

1. Collect YouTube scripts and save them in the `scripts/original/` folder
2. Mark sections in each lecture script with `#` markdown headers
3. Translate to Korean using GPT and Claude
4. Review and refine the translated content
5. Generate SRT subtitle files using `tools/txt_to_srt.py`

## How to Contribute

If you would like to contribute to this project, you can participate in the following ways:

1. Fix translation errors
2. Improve translation quality
3. Enhance SRT conversion tools
4. Add missing lecture scripts

## License Information

The original course is provided by MIT OpenCourseWare under a [Creative Commons License](https://ocw.mit.edu/terms/).

## Acknowledgements

- We thank Professor Gilbert Strang and the MIT OpenCourseWare team for making this excellent course publicly available.
- We appreciate all those who contributed to the translation and review process.

---

**Note**: This project was created for personal learning and educational purposes and is not used for commercial purposes.
