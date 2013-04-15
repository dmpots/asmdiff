	.section	__TEXT,__text,regular,pure_instructions
	.section	__TEXT,__textcoal_nt,coalesced,pure_instructions
	.section	__TEXT,__const_coal,coalesced
	.section	__TEXT,__picsymbolstub4,symbol_stubs,none,16
	.section	__TEXT,__StaticInit,regular,pure_instructions
	.syntax unified
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_one
	.align	2
	.code	16                      @ @one
	.thumb_func	_one
_one:
@ BB#0:
	bx	lr

	.globl	_two
	.align	2
	.code	16                      @ @two
	.thumb_func	_two
_two:
@ BB#0:
	bx	lr


.subsections_via_symbols
