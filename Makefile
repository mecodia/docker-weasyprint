timestamp := $(shell date -u +%FT%H-%MZ)
dh_repo := 'mecodia/weasyprint-server'

build:
	docker build --pull -t $(dh_repo):latest project