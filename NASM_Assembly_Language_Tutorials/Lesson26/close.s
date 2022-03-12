%include	'functions.s'

SECTION		.data
	filename		db		'readme.txt', 0h		; the filename to create
	contents		db		'Hello world!', 0h		; the contents to write

SECTION		.bss
	fileContents	resb	255,					; variable to store file contents

SECTION		.text
	global  _start

_start:
	mov		rsi, 0777			; Create file from lesson 22
	mov		rdi, filename
	mov		rax, 85
	syscall

	mov		rdx, 12				; Write contents to file from lesson 23
	mov		rsi, contents
	mov		rdi, rax
	mov		rax, 1
	syscall

	mov		rsi, 0				; Open file from lesson 24
	mov		rdi, filename
	mov		rax, 2
	syscall

	mov		rdx, 12				; Read file from lesson 25
	mov		rsi, fileContents
	mov		rdi, rax
	mov		rax, 0
	syscall

	mov		rax, fileContents
	call	sprintLF

	mov     rdi, rdi            ; not needed but used to demonstrate that SYS_CLOSE takes a file descriptor from rdi
	mov     rax, 3              ; invoke SYS_CLOSE (kernel opcode 3)
	syscall

	call	quit				; call our quit function
	