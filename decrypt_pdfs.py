from PyPDF2 import PdfFileWriter, PdfFileReader

# Create a PdfFileWriter object
out = PdfFileWriter()

# Open encrypted PDF file with the PdfFileReader
file = PdfFileReader("mi_archivo.pdf")

# Store correct password in a variable password.
password = "123456789"

# Check if the opened file is actually Encrypted
if file.isEncrypted:

	# If encrypted, decrypt it with the password
	file.decrypt(password)

	# Now, the file has been unlocked.
	# Iterate through every page of the file
	# and add it to our new file.
	for idx in range(file.numPages):
		
		# Get the page at index idx
		page = file.getPage(idx)
		
		# Add it to the output file
		out.addPage(page)
	
	# Open a new file "myfile_decrypted.pdf"
	with open("mi_archivo_decrypted.pdf", "wb") as f:
		
		# Write our decrypted PDF to this file
		out.write(f)

	# Print success message when Done
	print("File decrypted Successfully.")
else:
	
	# If file is not encrypted, print the
	# message
	print("File already decrypted.")
