# US-Missing-Persons-Database



## Dependencies

We use `requirements.txt` file as a lock file for complete package version control.  Running `make freeze` will update this file. We specify the minimum requirements of the app in `requirements.min.txt`, these are just the packages we _WANT_, excluding all of their dependencies. This makes it easier to add/remove pacakges we depend on.

### Adding a new pip package



```bash
# Add you're desired package to the `requirements.min.txt` file.
echo "pytorch==1.7" >> requirements.min.txt

# Then, run the install process.
make install

# Before making your final commits / PR, freeze the deps
make freeze
```