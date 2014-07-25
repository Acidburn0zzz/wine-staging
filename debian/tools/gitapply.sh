#
# Wrapper to apply binary patches without git.
#
# Copyright (C) 2014 Sebastian Lackner
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
#
	echo "Usage: ./gitapply [--nogit] [-v] [-d DIRECTORY]"
gitsha1()
{
	echo -en "blob $(du -b "$1" | cut -f1)\x00" | cat - "$1" | sha1sum | cut -d' ' -f1
}


		--nogit)
			nogit=1
			;;

		-v)
			verbose=1
			;;

			echo "Reverse applying patches not supported yet with this tool." >&2
			exit 1
# Check for missing depdencies
for dependency in awk chmod cut dd du gzip hexdump patch sha1sum; do
	if ! command -v "$dependency" >/dev/null 2>&1; then
		echo "Missing dependency: $dependency - please install this program and try again." >&2
		exit 1
	fi
done

# Detect BSD
	echo "This script is not compatible with *BSD utilities. Please install git," >&2
	echo "which provides the same functionality and will be used instead." >&2
	exit 1
		elif [ "${line:0:8}" == "old mode" ] || [ "${line:0:17}" == "deleted file mode" ]; then
		elif [ "${line:0:8}" == "new mode" ] || [ "${line:0:13}" == "new file mode" ]; then
			patch_errors+=("$lineno: Unable to parse header line '$line'.")
		elif [ "${line:0:9}" == "copy from" ] || [ "${line:0:7}" == "copy to" ]; then
			patch_errors+=("$lineno: Copy header not implemented yet.")
		elif [ "${line:0:7}" == "rename " ]; then
			patch_errors+=("$lineno: Patch rename header not implemented yet.")
		elif [ "${line:0:16}" == "similarity index" ] || [ "${line:0:19}" == "dissimilarity index" ]; then
		elif [ "${line:0:6}" == "index " ]; then
			patch_errors+=("$lineno: Unable to parse header line '$line'.")
				abort "Old name doesn't start with a/."
				abort "New name doesn't start with b/."
				patch_errors+=("$lineno: Missing index header, sha1 sums required for binary patch.")
				patch_errors+=("$lineno: Stripped old- and new name doesn't match for binary patch.")
		elif [ "${line:0:4}" == "@@ -" ]; then
		elif [ "${line:0:11}" == "diff --git " ]; then
				patch_errors+=("$lineno: Stripped old- and new name doesn't match.")
					sha=$(gitsha1 "$patch_oldname")
					echo "$lineno: Expected $patch_oldsha1" >&2
					echo "$lineno: Got      $sha" >&2
						[ "$arg1" -eq "$(du -b "$patch_oldname" | cut -f 1)" ] || break
						dd if="$patch_oldname" bs=1 skip="$arg1" count="$arg2" >> "$decoded_tmpfile" 2>/dev/null || break
						dd if="$patch_tmpfile" bs=1 skip="$arg1" count="$arg2" >> "$decoded_tmpfile" 2>/dev/null || break
			sha=$(gitsha1 "$patch_tmpfile")
				echo "$lineno: Expected $patch_newsha1" >&2
				echo "$lineno: Got      $sha" >&2
				abort "Unable to replace original file."
		elif [ "${line:0:2}" == "\\ " ]; then
			# ignore
			echo "$line" >> "$patch_tmpfile"
			continue

		if [ "${line:0:1}" == " " ] && [ "$hunk_src_lines" -gt 0 ] && [ "$hunk_dst_lines" -gt 0 ]; then
		elif [ "${line:0:1}" == "-" ] && [ "$hunk_src_lines" -gt 0 ]; then
		elif [ "${line:0:1}" == "+" ] && [ "$hunk_dst_lines" -gt 0 ]; then
		elif [ "${line:0:2}" == "\\ " ]; then
			abort "Unexpected line in hunk."
		elif [ "${line:0:4}" == "@@ -" ] || [ "${line:0:4}" == "--- " ] || [ "${line:0:4}" == "+++ " ]; then