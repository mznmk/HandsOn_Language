%include	'functions.s'

section		.data
	msg1	db		' remainder '	; a message string to correctly output result
section		.text
	global	_start

_start:
	mov		rax, 90		; move our first number into rax
	mov		rbx, 9		; move our second number into rbx
	mov		rdx, 0
	div		rbx
	call	iprint
	mov		rax, msg1
	call	sprint
	mov		rax, rdx
	call	iprintLF

	call	quit
