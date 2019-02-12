SUBDIRS := qubes-mate-dom0

help:
	@echo "make rpms        -- generate binary rpm packages"
	@echo "make srpms       -- generate source rpm packages"


get-sources verify-sources:
	@for dir in garcon xfwm4; do \
	    $(MAKE) -C $$dir $@ || exit 1;\
	done

%:
	@for dir in $(SUBDIRS); do \
	    $(MAKE) -C $$dir $* || exit 1;\
	done
