mode: command
-
# Copy selection to clipboard
edit copy: edit.copy()
# Cut selection to clipboard
edit cut: edit.cut()
# Delete selection
edit delete: edit.delete()
# Delete line under cursor
# edit command: edit.delete_line()
# Delete paragraph under cursor
# edit command: edit.delete_paragraph()
# Delete sentence under cursor
# edit command: edit.delete_sentence()
# Delete word under cursor
# edit command: edit.delete_word()
# Move cursor down one row
edit row down: edit.down()
# Extend selection again in the same way
# edit command: edit.extend_again()
# Extend selection to column <n>
# edit command: edit.extend_column()
# Extend selection down one row
# edit command: edit.extend_down()
# Extend selection to end of file
edit select to end of file: edit.extend_file_end()
# Extend selection to start of file
edit select to start of file: edit.extend_file_start()
# Extend selection left one column
edit select left: edit.extend_left()
# Extend selection to include line <n>
# edit command: edit.extend_line()
# Extend selection down one full line
edit select down: edit.extend_line_down()
# Extend selection to end of line
edit select to end of line: edit.extend_line_end()
# Extend selection to start of line
edit select to start of line: edit.extend_line_start()
# Extend selection up one full line
edit select up: edit.extend_line_up()
# Extend selection down one page
edit select page down: edit.extend_page_down()
# Extend selection up one page
edit select page up: edit.extend_page_up()
# Extend selection to the end of the current paragraph
# edit command: edit.extend_paragraph_end()
# Extend selection to the start of the next paragraph
# edit command: edit.extend_paragraph_next()
# Extend selection to the start of the previous paragraph
# edit command: edit.extend_paragraph_previous()
# Extend selection to the start of the current paragraph
# edit command: edit.extend_paragraph_start()
# Extend selection right one column
edit select right: edit.extend_right()
# Extend selection to the end of the current sentence
# edit command: edit.extend_sentence_end()
# Extend selection to the start of the next sentence
# edit command: edit.extend_sentence_next()
# Extend selection to the start of the previous sentence
# edit command: edit.extend_sentence_previous()
# Extend selection to the start of the current sentence
# edit command: edit.extend_sentence_start()
# Extend selection up one row
# edit command: edit.extend_up()
# Extend selection left one word
edit select word left: edit.extend_word_left()
# Extend selection right one word
edit select word right: edit.extend_word_right()
# Move cursor to end of file (start of line)
edit go to end of file: edit.file_end()
# Move cursor to start of file
edit go to start of file: edit.file_start()
# Open Find dialog, optionally searching for text
edit start search: edit.find()
# Select next Find result
edit find next: edit.find_next()
# Select previous Find result
edit find previous: edit.find_previous()
# Remove a tab stop of indentation
edit unindent: edit.indent_less()
# Add a tab stop of indentation
edit indent: edit.indent_more()
# Move cursor to column <n>
# edit command: edit.jump_column()
# Move cursor to line <n>
edit go to line <number>: edit.jump_line(number)
# Move cursor left one column
edit left: edit.left()
# Create a new line identical to the current line
# edit command: edit.line_clone()
# Move cursor to start of line below
edit line down: edit.line_down()
# Move cursor to end of line
edit end of line: edit.line_end()
# Insert line below cursor
# edit command: edit.line_insert_down()
# Insert line above cursor
# edit command: edit.line_insert_up()
# Move cursor to start of line
edit start of line: edit.line_start()
# Swap the current line with the line below
# edit command: edit.line_swap_down()
# Swap the current line with the line above
# edit command: edit.line_swap_up()
# Move cursor to start of line above
edit line up: edit.line_up()
# Move cursor again in the same way
# edit command: edit.move_again()
# Move cursor down one page
edit page down: edit.page_down()
# Move cursor up one page
edit page up: edit.page_up()
# Move cursor to the end of the current paragraph
# edit command: edit.paragraph_end()
# Move cursor to the start of the next paragraph
# edit command: edit.paragraph_next()
# Move cursor to the start of the previous paragraph
# edit command: edit.paragraph_previous()
# Move cursor to the start of the current paragraph
# edit command: edit.paragraph_start()
# Paste clipboard at cursor
edit paste: edit.paste()
# Paste clipboard without style information
# edit command: edit.paste_match_style()
# Open print dialog
edit print: edit.print()
# Redo
edit redo: edit.redo()
# Move cursor right one column
edit right: edit.right()
# Save current document
edit save: edit.save()
# Save all open documents
edit save all: edit.save_all()
# Select all text in the current document
edit select all: edit.select_all()
# Select entire line <n>, or current line
# edit command: edit.select_line()
# Select entire lines from <a> to <b>
# edit command: edit.select_lines()
# Clear current selection
# edit command: edit.select_none()
# Select the entire nearest paragraph
# edit command: edit.select_paragraph()
# Select the entire nearest sentence
# edit command: edit.select_sentence()
# Select word under cursor
# edit command: edit.select_word()
# Get currently selected text
# edit command: edit.selected_text()
# Insert a copy of the current selection
# edit command: edit.selection_clone()
# Move cursor to the end of the current sentence
# edit command: edit.sentence_end()
# Move cursor to the start of the next sentence
# edit command: edit.sentence_next()
# Move cursor to the start of the previous sentence
# edit command: edit.sentence_previous()
# Move cursor to the start of the current sentence
# edit command: edit.sentence_start()
# Undo
edit undo: edit.undo()
# Move cursor up one row
edit row up: edit.up()
# Move cursor left one word
edit word left: edit.word_left()
# Move cursor right one word
edit word right: edit.word_right()
# Zoom in
edit zoom in: edit.zoom_in()
# Zoom out
edit zoom out: edit.zoom_out()
# Zoom to original size
edit zoom reset: edit.zoom_reset()
