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

# No extras are packaged. peft is pulled in only as a runtime dependency (LoRA
# support); its dev/docs-specific/quality/test extras add nothing vLLM needs and
# are unbuildable here (they require diffusers, hf-doc-builder, parameterized and
# ruff, none of which are packaged). peft's core deps (torch, transformers,
# accelerate, safetensors, huggingface-hub, numpy, ...) are enough.


%prep
%autosetup -p1 -n peft-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l peft


%check
# Exclude optional tuner backends whose imports need unpackaged deps: the *.bnb
# modules are bitsandbytes quantization backends (import bitsandbytes) and
# lora.corda is a CorDA init method (import attr). None is used unless the extra
# dep is present; every other peft module is still import-checked. All -e flags
# must stay on one line -- pyproject_check_import parses its options with a Lua
# getopt over the macro's args, and a backslash line-continuation makes it see an
# empty option list, silently dropping the excludes.
%pyproject_check_import -e peft.tuners.hira.bnb -e peft.tuners.lora.bnb -e peft.tuners.lora.corda -e peft.tuners.oft.bnb -e peft.tuners.pvera.bnb -e peft.tuners.randlora.bnb -e peft.tuners.road.bnb


%files -n python3-peft -f %{pyproject_files}


%changelog
%autochangelog
