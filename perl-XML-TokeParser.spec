%define upstream_name XML-TokeParser
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	0.05
Release:	3
Summary:	Simplified interface to XML::Parser
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-TokeParser
Source0:	https://cpan.metacpan.org/authors/id/P/PO/PODMASTER/XML-TokeParser-0.05.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch

%description
XML::TokeParser provides a procedural (pull mode) interface to XML::Parser.

%prep
%setup -q -n XML-TokeParser-0.05

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test || :

%install
%makeinstall_std

%files
%doc Changes META.yml README TODO
%{perl_vendorlib}/XML
%{_mandir}/man3/*
