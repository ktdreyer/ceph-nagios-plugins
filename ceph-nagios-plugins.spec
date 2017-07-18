%global commitdate 20170718
%global commit ae886b755398329d8c99a6cd5fd5fe376e9171a9
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# Package needs to stay arch specific (due to nagios plugins location), but
# there's nothing to extract debuginfo from
%global debug_package %{nil}

%global nagios_plugins_dir %{_libdir}/nagios/plugins

Name:          ceph-nagios-plugins
Version:       1.5.0
Release:       1.%{commitdate}git%{shortcommit}%{?dist}
Summary:       Nagios plugins for Ceph
License:       ASL 2.0
URL:           https://github.com/valerytschopp/ceph-nagios-plugins
Source0:       https://github.com/valerytschopp/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

%description
A set of plugins to monitor a Ceph cluster.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build

%install
make install DESTDIR=%{buildroot} libdir=%{_libdir} sysconfdir=%{_sysconfdir}

%files
%license COPYRIGHT LICENSE
%doc README.md CHANGELOG
%config(noreplace) %{_sysconfdir}/nagios-plugins/config/ceph.cfg
%{nagios_plugins_dir}/check_ceph_df
%{nagios_plugins_dir}/check_ceph_health
%{nagios_plugins_dir}/check_ceph_mds
%{nagios_plugins_dir}/check_ceph_mon
%{nagios_plugins_dir}/check_ceph_osd
%{nagios_plugins_dir}/check_ceph_rgw

%changelog
* Tue Jul 18 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.5.0-1.20170718gitae886b7
- initial package (git snapshot from master)
