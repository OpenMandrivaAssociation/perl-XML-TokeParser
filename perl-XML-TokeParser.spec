%define module 	XML-TokeParser
%define version 0.05
%define release %mkrel 3

Summary:	Simplified interface to XML::Parser
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} 
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} PREFIX=$RPM_BUILD_ROOT%{_prefix} install


%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README MANIFEST Changes 
%{_mandir}/*/*
%{perl_vendorlib}/XML/*

