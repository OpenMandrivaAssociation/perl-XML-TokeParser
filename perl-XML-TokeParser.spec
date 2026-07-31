%define upstream_name 	 XML-TokeParser
%define upstream_version 0.05
Name: 		perl-%{upstream_name}
Version:	0.05
Release:	5

Summary:	Simplified interface to XML::Parser
License: 	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/XML-TokeParser
Source0:	https://cpan.metacpan.org/authors/id/P/PO/PODMASTER/XML-TokeParser-0.05.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The XML::TokeParser perl module provides a procedural ("pull mode")
interface to XML::Parser in much the same way that HTML::TokeParser
provides a procedural interface to HTML::Parser.

XML::TokeParser splits its XML input up into "tokens," each
corresponding to an XML::Parser event.

A token is a reference to an array whose first element is an event-type 
string and whose last element is the literal text of the XML input that 
generated the event, with intermediate elements varying according to the 
event type:


%prep
%setup -q -n XML-TokeParser-0.05

%build
perl Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} 
%{__make}

%install
%{__make} PREFIX=%{buildroot}%{_prefix} install


%files
%doc README MANIFEST Changes 
%{_mandir}/*/*
%{perl_vendorlib}/XML/*


