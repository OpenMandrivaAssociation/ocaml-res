Name:           ocaml-res
Version:        3.2.0
Release:        %mkrel 1
Summary:        Library for automatically resizing contiguous memory (arrays and strings)
License:        LGPL
Group:          Development/Other
URL:            http://ocaml.info/home/ocaml_sources.html#res
Source:         http://hg.ocaml.info/release/res/archive/res-release-%{version}.tar.bz2
# curl http://hg.ocaml.info/release/res/archive/release-%{version}.tar.bz2 > res-release-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  tetex-latex
BuildRequires:  texlive-texmf-cmsuper
BuildRequires:  ghostscript
BuildRequires:  ghostscript-common

%description
This OCaml-library consists of a set of modules which implement
automatically resizing (= reallocating) datastructures that consume
a contiguous part of memory. This allows appending and removing of
elements to/from arrays (both boxed and unboxed), strings (-> buffers),
bit strings and weak arrays while still maintaining fast constant-time
access to elements.

There are also functors that allow the generation of similar modules
which use different reallocation strategies.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n res-release-%{version}

%build
make
make doc

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/res
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
%dir %{_libdir}/ocaml/res
%{_libdir}/ocaml/res/META
%{_libdir}/ocaml/res/*.cma
%{_libdir}/ocaml/res/*.cmi

%files devel
%defattr(-,root,root)
%doc LICENSE Changelog INSTALL README.txt TODO
%doc doc/res/{html,latex} examples/
%{_libdir}/ocaml/res/*.a
%{_libdir}/ocaml/res/*.cmxa
%{_libdir}/ocaml/res/*.mli

