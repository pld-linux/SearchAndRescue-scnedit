Summary:	Search And Rescue scenery editor
Summary(pl):	Edytor scenerii gry Search And Rescue
Name:		SearchAndRescue-scnedit
%define	rname	scnedit
Version:	0.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{rname}-%{version}.tar.bz2
# Source0-md5:	19b7e9ce36ad0d83f5f21d323b0b5c84
URL:		http://wolfpack.twu.net/SearchAndRescue/
BuildRequires:	gtk+-devel >= 1.2.10
Requires:	SearchAndRescue >= 0.7.21
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scenery Editor (scnedit) allows you to edit the scenery files (.scn
files) for the game Search and Rescue.

%description -l pl
Scenery Editor (scnedit) pozwala na edycjê plików scenerii (.scn) dla
gry Search And Rescue.

%prep
%setup -q -n %{rname}-%{version}

%build
# not autoconf-generated
./configure Linux -v

%{__make} \
	CFLAGS="%{rpmcflags} `gtk-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man6 \
	DATA_DIR=$RPM_BUILD_ROOT%{_datadir}/SearchAndRescue/scnedit

bzip2 -d $RPM_BUILD_ROOT%{_mandir}/man6/*.bz2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*.6*
