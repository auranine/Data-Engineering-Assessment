Order Analytics
===============

## Prerequisites*

-------------

- uv

__* Note:__ This project configuration and development instructions here have been tested on Mac OS. 
Linux and Windows specific and changes are welcome contributions! 

---------------

## Setup
1. Install uv (see: [official uv site](https://docs.astral.sh))
2. Verify Installation (make sure you open a new shell or source your *rc file)
        
       ➜  app git:(main) ✗ uv --version
       uv 0.9.5 (d5f39331a 2025-10-21)
3. Within `app` directory
   1. Install python - `uv python install`  
   
            ➜  app git:(main) ✗ uv python install
            Installed Python 3.12.6 in 45ms
               + cpython-3.12.6-macos-aarch64-none (python3.12)
   2. Sync dependencies - `uv sync`  

            ➜  app git:(main) ✗ uv sync
            Resolved 20 packages in 6ms
            Audited 18 packages in 3ms
4. Configure your IDE:
   1. Docstring format to Google
   2. Intellij Specific
      1. Right click on `src` and mark as source
      2. Right click on `test` and mark as test source
5. Run Tests:
   1. `uv run pytest`


