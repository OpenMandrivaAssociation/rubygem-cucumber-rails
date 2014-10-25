%define rbname cucumber-rails

Summary:	Cucumber Generators and Runtime for Rails
Name:		rubygem-%{rbname}
Version:	1.4.1
Release:	1
License:	MIT
Group:		Development/Ruby
Url:		http://github.com/aslakhellesoy/%{rbname}
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems
Suggests:	rubygem(aruba)
BuildArch:	noarch

%description
Cucumber Generators and Runtime for Rails.

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
Conflicts:	%{name} < 1.4.1

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install



