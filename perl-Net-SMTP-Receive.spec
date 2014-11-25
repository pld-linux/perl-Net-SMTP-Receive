%define		pdir	Net
%define		pnam	SMTP-Receive
%include	/usr/lib/rpm/macros.perl
Summary:	Net::SMTP::Receive - receive mail via SMTP
Summary(pl.UTF-8):	Net::SMTP::Receive - odbieranie poczty protokołem SMTP
Name:		perl-Net-SMTP-Receive
Version:	0.3
Release:	4
License:	Public Domain
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0863aa1ee5f5950dc9e13b06927aea90
URL:		http://search.cpan.org/dist/Net-SMTP-Receive/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SMTP::Receive handles receiving email via SMTP. It is built as a
base class that must be subclassed to provide methods for actually
delivering a message. Many aspects of Net::SMTP::Receive's behavior
can be modified by overriding methods in the subclass.

%description -l pl.UTF-8
Moduł Net::SMTP::Receive obsługuje odbieranie poczty po SMTP. Jest
zbudowany jako klasa bazowa, z której należy dziedziczyć, aby
udostępnić metody do właściwego dostarczania wiadomości. Wiele
aspektów zachowania Net::SMTP::Receive może być modyfikowanych poprzez
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
