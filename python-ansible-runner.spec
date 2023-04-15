# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-ansible-runner
Epoch: 100
Version: 2.3.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Tool and python library to interface with Ansible
License: Apache-2.0
URL: https://github.com/ansible/ansible-runner/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Ansible Runner is a tool and python library that helps when interfacing
with Ansible from other systems whether through a container image
interface, as a standalone tool, or imported into a python project.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-ansible-runner
Summary: Tool and python library to interface with Ansible
Requires: python3
Requires: python3-daemon
Requires: python3-pexpect >= 4.5
Requires: python3-psutil
Requires: python3-PyYAML
Requires: python3-six
Provides: python3-ansible-runner = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-runner) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-runner = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-runner) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-runner = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-runner) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-ansible-runner
Ansible Runner is a tool and python library that helps when interfacing
with Ansible from other systems whether through a container image
interface, as a standalone tool, or imported into a python project.

%files -n python%{python3_version_nodots}-ansible-runner
%license LICENSE.md
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-ansible-runner
Summary: Tool and python library to interface with Ansible
Requires: python3
Requires: python3-daemon
Requires: python3-pexpect >= 4.5
Requires: python3-psutil
Requires: python3-PyYAML
Requires: python3-six
Provides: python3-ansible-runner = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-runner) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-runner = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-runner) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-runner = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-runner) = %{epoch}:%{version}-%{release}

%description -n python3-ansible-runner
Ansible Runner is a tool and python library that helps when interfacing
with Ansible from other systems whether through a container image
interface, as a standalone tool, or imported into a python project.

%files -n python3-ansible-runner
%license LICENSE.md
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-ansible-runner
Summary: Tool and python library to interface with Ansible
Requires: python3
Requires: python3-daemon
Requires: python3-pexpect >= 4.5
Requires: python3-psutil
Requires: python3-pyyaml
Requires: python3-six
Provides: python3-ansible-runner = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-runner) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-runner = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-runner) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-runner = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-runner) = %{epoch}:%{version}-%{release}

%description -n python3-ansible-runner
Ansible Runner is a tool and python library that helps when interfacing
with Ansible from other systems whether through a container image
interface, as a standalone tool, or imported into a python project.

%files -n python3-ansible-runner
%license LICENSE.md
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
