%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Library for automatically resizing contiguous memory (arrays and strings)
Name:		ocaml-res
Version:	4.0.3
Release:	2
License:	LGPLv2.1+
Group:		Development/Other
Url:		http://ocaml.info/home/ocaml_sources.html#res
Source0:	http://hg.ocaml.info/release/res/archive/res-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
This OCaml-library consists of a set of modules which implement
automatically resizing (= reallocating) datastructures that consume
a contiguous part of memory. This allows appending and removing of
elements to/from arrays (both boxed and unboxed), strings (-> buffers),
bit strings and weak arrays while still maintaining fast constant-time
access to elements.

There are also functors that allow the generation of similar modules
which use different reallocation strategies.

%files
%doc AUTHORS.txt CHANGES.txt COPYING.txt
%dir %{_libdir}/ocaml/res
%{_libdir}/ocaml/res/META
%{_libdir}/ocaml/res/*.cma
%{_libdir}/ocaml/res/*.cmi
%{_libdir}/ocaml/res/*.cmxs

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc examples/
%{_libdir}/ocaml/res/*.a
%{_libdir}/ocaml/res/*.cmx
%{_libdir}/ocaml/res/*.cmxa
%{_libdir}/ocaml/res/*.ml
%{_libdir}/ocaml/res/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n res-%{version}

%build
./configure --prefix=%{_prefix}
make

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/res
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install

