%include	'functions.s'

SECTION		.data
	filename		db		'readme.txt', 0h		; the filename to create

SECTION		.text
	global  _start

_start:
	mov		rdi, filename		; filename we will delete
	mov		rax, 87				; invoke SYS_UNLINK (kernel opcode 87)
	syscall

	call	quit				; call our quit function
	