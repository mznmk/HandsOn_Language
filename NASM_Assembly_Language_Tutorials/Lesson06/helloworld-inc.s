%include	'functions.s'										; include our external file

section		.data
	msg1	db		'Hello, brave new world!', 0Ah, 0h			; our first message string
	msg2	db		'This is how we recycle in NASM.', 0Ah, 0h	; our second message string

section		.text
	global	_start

_start:
	mov		rax, msg1
	call	sprint

	mov		rax, msg2
	call	sprint

	call	quit
