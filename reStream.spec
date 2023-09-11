%define debug_package %{nil}

Name:           reStream
Version:        1.2.0
Release:        %autorelease
URL:            https://github.com/rien/reStream
Source:         %{url}/archive/%{version}/restream-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/thebeanogamer/reStream/main/reStream_helptext.patch
Summary:        Stream your reMarkable screen over SSH
License:        MIT
BuildArch:      noarch

Requires:       /usr/bin/sh
Requires:       openssh-clients
Requires:       ffmpeg >= 4.0.0
Requires:       lz4

%description
Stream your reMarkable screen over SSH

%prep
%autosetup -n reStream-%{version}

%build
ln -s reStream.sh reStream
help2man -N ./reStream -o reStream.1 
rm -f reStream

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 reStream.sh %{buildroot}%{_bindir}/reStream
mkdir -p %{buildroot}%{_mandir}/man1/
install -pm 0644 reStream.1 %{buildroot}%{_mandir}/man1/reStream.1

%files
%license LICENSE
%doc README.md
%{_bindir}/reStream
%{_mandir}/man1/reStream.1*

%changelog
%autochangelog
