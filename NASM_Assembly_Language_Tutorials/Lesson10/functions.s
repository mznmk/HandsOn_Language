;--------------------------------------------------
; int slen(String message)
; String lenght calculation function
;--------------------------------------------------
slen:
	push	rbx
	mov		rbx, rax

nextchar:
	cmp		byte [rax], 0
	jz		finished
	inc		rax
	jmp		nextchar

finished:
	sub		rax, rbx
	pop		rbx
	ret

;--------------------------------------------------
; void sprint(String message)
; String printing function
;--------------------------------------------------
sprint:
	push	rdx
	push	rsi
	push	rdi
	push	rax

	call	slen

	mov		rdx, rax
	pop		rax
	mov		rsi, rax
	mov		rdi, 1
	mov		rax, 1
	syscall

	pop		rdi
	pop		rsi
	pop		rdx
	ret

;--------------------------------------------------
; void sprintLF(String message)
; String printing with line feed function
;--------------------------------------------------
sprintLF:
	call 	sprint

	push	rax				; push RAX onto the stack to preserve it while we use the RAX register in this function
	mov		rax, 0Ah		; move 0Ah into RAX - 0Ah is the ascii character for a linefeed
	push	rax				; push the linefeed onto the stack so we can get the address
	mov		rax, rsp		; move the address of the current stack pointer into RAX for sprint
	call	sprint			; call our sprint function
	pop		rax				; remove our linefeed character from the stack
	pop		rax				; restore the original value of RAX before our function was called
	ret						; return to our program

;--------------------------------------------------
; void exit()
; Exit program and restore resources
;--------------------------------------------------
quit:
	mov		rax, 60
	mov		rdi, 0
	syscall
	ret
