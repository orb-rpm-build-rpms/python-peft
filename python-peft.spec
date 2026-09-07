Name:           python-peft
Version:        0.20.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Parameter-Efficient Fine-Tuning _PEFT_

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/huggingface/peft
Source:         %{pypi_source peft}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'peft' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-peft
Summary:        %{summary}

%description -n python3-peft %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-peft dev,docs-specific,quality,test


%prep
%autosetup -p1 -n peft-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,docs-specific,quality,test


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l peft


%check
%pyproject_check_import


%files -n python3-peft -f %{pyproject_files}


%changelog
%autochangelog
