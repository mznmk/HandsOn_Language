%include	'functions.s'

section		.text
	global	_start

_start:
	mov		rbx, 0

nextNumber:
	inc		rbx
	mov		rax, rbx
	call	iprintLF		; NOTE call our new integer printing function (itoa)
	cmp		rbx, 10
	jne		nextNumber

	call	quit
