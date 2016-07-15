Name:     ocaml-alsa

Version:  0.2.2
Release:  1
Summary:  OCaml interface to alsa library/asound2
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-alsa
Source0:  https://github.com/savonet/ocaml-alsa/releases/download/0.2.2/ocaml-alsa-0.2.2.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: alsa-lib-devel
Requires:      alsa-lib

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export OCAMLFIND_LDCONF=ignore
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
make install

%files
/usr/lib64/ocaml/alsa/META
/usr/lib64/ocaml/alsa/alsa.a
/usr/lib64/ocaml/alsa/alsa.cma
/usr/lib64/ocaml/alsa/alsa.cmi
/usr/lib64/ocaml/alsa/alsa.cmx
/usr/lib64/ocaml/alsa/alsa.cmxa
/usr/lib64/ocaml/alsa/alsa.mli

%description
This package contains an O'Caml interface for alsa library, otherwise known as libasound2.

%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-alsa.spec
