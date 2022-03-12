%include	'functions.s'

section		.text
	global	_start

_start:
	mov		rax, 90		; move our first number into rax
	mov		rbx, 9		; move our second number into rbx
	mul		rbx			; multiply rax by rbx
	call	iprintLF	; call our integer print with linefeed function

	call	quit
