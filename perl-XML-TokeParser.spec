%define upstream_name 	 XML-TokeParser
%define upstream_version 0.05

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	2

Summary:	Simplified interface to XML::Parser
License: 	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} 
%{__make}

%install
%{__make} PREFIX=%{buildroot}%{_prefix} install


%files
%doc README MANIFEST Changes 
%{_mandir}/*/*
%{perl_vendorlib}/XML/*


%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 401849
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.05-6mdv2009.0
+ Revision: 242274
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.05-4mdv2008.0
+ Revision: 23483
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.05-3mdk
- Fix According to perl Policy
	- Source URL
	- URL
- use mkrel

* Wed Sep 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.05-2mdk
- rebuild

* Wed Aug 27 2003 François Pons <fpons@mandrakesoft.com> 0.05-1mdk
- 0.05.

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-5mdk
- rebuild for new auto{prov,req}

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-4mdk
- rebuild for new auto{prov,req}

