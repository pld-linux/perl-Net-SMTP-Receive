%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	SMTP-Receive
Summary:	Net::SMTP::Receive - receive mail via SMTP
Summary(pl):	Net::SMTP::Receive - odbieranie poczty protoko³em SMTP
Name:		perl-Net-SMTP-Receive
Version:	0.3
Release:	3
License:	Public Domain
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0863aa1ee5f5950dc9e13b06927aea90
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SMTP::Receive handles receiving email via SMTP.  It is built as
a base class that must be subclassed to provide methods for actually
delivering a message.  Many aspects of Net::SMTP::Receive's behavior
can be modified by overriding methods in the subclass.

%description -l pl
Modu³ Net::SMTP::Receive obs³uguje odbieranie poczty po SMTP. Jest
zbudowany jako klasa bazowa, z której nale¿y dziedziczyæ, aby
udostêpniæ metody do w³a¶ciwego dostarczania wiadomo¶ci. Wiele
aspektów zachowania Net::SMTP::Receive mo¿e byæ modyfikowanych poprzez
pokrywanie metod w podklasie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp example_daemon.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Net/SMTP/*.pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
