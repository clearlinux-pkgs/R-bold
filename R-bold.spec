#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bold
Version  : 0.9.0
Release  : 17
URL      : https://cran.r-project.org/src/contrib/bold_0.9.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bold_0.9.0.tar.gz
Summary  : Interface to Bold Systems API
Group    : Development/Tools
License  : MIT
Requires: R-crul
Requires: R-data.table
Requires: R-jsonlite
Requires: R-plyr
Requires: R-reshape
Requires: R-stringr
Requires: R-tibble
Requires: R-vcr
Requires: R-xml2
BuildRequires : R-crul
BuildRequires : R-data.table
BuildRequires : R-jsonlite
BuildRequires : R-plyr
BuildRequires : R-reshape
BuildRequires : R-stringr
BuildRequires : R-tibble
BuildRequires : R-vcr
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
bold
====
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![cran version](https://www.r-pkg.org/badges/version/bold)](https://cran.r-project.org/package=bold)

%prep
%setup -q -c -n bold

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569219197

%install
export SOURCE_DATE_EPOCH=1569219197
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bold
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bold
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bold
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc bold || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bold/DESCRIPTION
/usr/lib64/R/library/bold/INDEX
/usr/lib64/R/library/bold/LICENSE
/usr/lib64/R/library/bold/Meta/Rd.rds
/usr/lib64/R/library/bold/Meta/data.rds
/usr/lib64/R/library/bold/Meta/features.rds
/usr/lib64/R/library/bold/Meta/hsearch.rds
/usr/lib64/R/library/bold/Meta/links.rds
/usr/lib64/R/library/bold/Meta/nsInfo.rds
/usr/lib64/R/library/bold/Meta/package.rds
/usr/lib64/R/library/bold/Meta/vignette.rds
/usr/lib64/R/library/bold/NAMESPACE
/usr/lib64/R/library/bold/NEWS.md
/usr/lib64/R/library/bold/R/bold
/usr/lib64/R/library/bold/R/bold.rdb
/usr/lib64/R/library/bold/R/bold.rdx
/usr/lib64/R/library/bold/data/Rdata.rdb
/usr/lib64/R/library/bold/data/Rdata.rds
/usr/lib64/R/library/bold/data/Rdata.rdx
/usr/lib64/R/library/bold/doc/bold.Rmd
/usr/lib64/R/library/bold/doc/bold.html
/usr/lib64/R/library/bold/doc/index.html
/usr/lib64/R/library/bold/help/AnIndex
/usr/lib64/R/library/bold/help/aliases.rds
/usr/lib64/R/library/bold/help/bold.rdb
/usr/lib64/R/library/bold/help/bold.rdx
/usr/lib64/R/library/bold/help/paths.rds
/usr/lib64/R/library/bold/html/00Index.html
/usr/lib64/R/library/bold/html/R.css
/usr/lib64/R/library/bold/tests/fixtures/bold_filter.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_identify_ampersands.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_identify_db_param.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_identify_parents.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_identify_parents_wide.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_identify_parents_wrong_type.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_identify_response_param.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_identify_works.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_seq_works_bin.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_seq_works_taxon.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_seq_works_taxon_response.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_seqspec_one.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_seqspec_three.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_seqspec_two.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_specimens_response.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_stats.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_stats_many_taxa.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_stats_response_true.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_tax_id1.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_tax_id2.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_tax_id_datatypes_param_basic.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_tax_id_datatypes_param_geo.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_tax_id_datatypes_param_multiple.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_tax_id_datatypes_param_sequencinglabs.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_tax_id_datatypes_param_stats1.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_tax_id_datatypes_param_stats2.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_tax_id_includetree_param.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_tax_id_multiple_ids.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_tax_name.yml
/usr/lib64/R/library/bold/tests/fixtures/bold_tax_name_fuzzy.yml
/usr/lib64/R/library/bold/tests/test-all.R
/usr/lib64/R/library/bold/tests/testthat/bold_identify_list.rda
/usr/lib64/R/library/bold/tests/testthat/helper-bold.R
/usr/lib64/R/library/bold/tests/testthat/test-bold_filter.R
/usr/lib64/R/library/bold/tests/testthat/test-bold_identify.R
/usr/lib64/R/library/bold/tests/testthat/test-bold_identify_parents.R
/usr/lib64/R/library/bold/tests/testthat/test-bold_seq.R
/usr/lib64/R/library/bold/tests/testthat/test-bold_seqspec.R
/usr/lib64/R/library/bold/tests/testthat/test-bold_specimens.R
/usr/lib64/R/library/bold/tests/testthat/test-bold_stats.R
/usr/lib64/R/library/bold/tests/testthat/test-bold_tax_id.R
/usr/lib64/R/library/bold/tests/testthat/test-bold_tax_name.R
