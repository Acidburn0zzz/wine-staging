import email.header
import shutil
_devnull = open(os.devnull, 'wb')

    def __init__(self, filename, header):
        self.patch_author       = header['author']
        self.patch_email        = header['email']
        self.patch_subject      = header['subject']
        self.patch_revision     = header['revision'] if header.has_key('revision') else 1

        # self.extracted_patch    = None
        self.unique_hash        = None
        self.filename           = filename
        self.offset_begin       = None
        self.offset_end         = None
        self.isbinary           = False
        self.oldname            = None
        self.newname            = None
        self.modified_file      = None
        self.oldsha1            = None
        self.newsha1            = None
        self.newmode            = None
                buf = fp.read(16384 if i > 16384 else i)
class _FileReader(object):
    def __init__(self, filename):
        self.filename = filename
        self.fp       = open(self.filename)
        self.peeked   = None

    def close(self):
        self.fp.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def seek(self, pos):
        """Change the file cursor position."""
        self.fp.seek(pos)
        self.peeked = None

    def tell(self):
        """Return the current file cursor position."""
        if self.peeked is None:
            return self.fp.tell()
        return self.peeked[0]

    def peek(self):
        """Read one line without changing the file cursor."""
        if self.peeked is None:
            pos = self.fp.tell()
            tmp = self.fp.readline()
            if len(tmp) == 0: return None
            self.peeked = (pos, tmp)
        return self.peeked[1]

    def read(self):
        """Read one line from the file, and move the file cursor to the next line."""
        if self.peeked is None:
            tmp = self.fp.readline()
            if len(tmp) == 0: return None
            return tmp
        tmp, self.peeked = self.peeked, None
        return tmp[1]
    def _read_single_patch(fp, header, oldname=None, newname=None):
        patch = PatchObject(fp.filename, header)











    def _parse_author(author):
        author = ' '.join([data.decode(format or 'utf-8').encode('utf-8') for \
                          data, format in email.header.decode_header(author)])
        r =  re.match("\"?([^\"]*)\"? <(.*)>", author)
        if r is None: raise NotImplementedError("Failed to parse From - header.")
        return r.group(1).strip(), r.group(2).strip()

    def _parse_subject(subject):
        version = "(v|try|rev|take) *([0-9]+)"
        subject = subject.strip()
        if subject.endswith("."): subject = subject[:-1]
        r = re.match("^\\[PATCH([^]]*)\\](.*)$", subject, re.IGNORECASE)
        if r is not None:
            subject = r.group(2).strip()
            r = re.search(version, r.group(1), re.IGNORECASE)
            if r is not None: return subject, int(r.group(2))
        r = re.match("^(.*)\\(%s\\)$" % version, subject, re.IGNORECASE)
        if r is not None: return r.group(1).strip(), int(r.group(3))
        r = re.match("^(.*)[.,] +%s$" % version, subject, re.IGNORECASE)
        if r is not None: return r.group(1).strip(), int(r.group(3))
        r = re.match("^([^:]+) %s: (.*)$" % version, subject, re.IGNORECASE)
        if r is not None: return "%s: %s" % (r.group(1), r.group(4)), int(r.group(3))
        r = re.match("^(.*) +%s$" % version, subject, re.IGNORECASE)
        if r is not None: return r.group(1).strip(), int(r.group(3))
        return subject, 1

    header = {}

            elif line.startswith("From: "):
                header['author'], header['email'] = _parse_author(line[6:])
                assert fp.read() == line

            elif line.startswith("Subject: "):
                subject = line[9:].rstrip("\r\n")
                assert fp.read() == line
                while True:
                    line = fp.peek()
                    if not line.startswith(" "): break
                    subject += line.rstrip("\r\n")
                    assert fp.read() == line
                subject, revision = _parse_subject(subject)
                if not subject.endswith("."): subject += "."
                header['subject'], header['revision'] = subject, revision

                yield _read_single_patch(fp, header, tmp[2].strip(), tmp[3].strip())

                yield _read_single_patch(fp, header)


def apply_patch(original, patchfile, reverse=False, fuzz=2):
    result = tempfile.NamedTemporaryFile(delete=False)
        # We open the file again to avoid race-conditions with multithreaded reads
        with open(original.name) as fp:
            shutil.copyfileobj(fp, result)
        result.close()

        cmdline = ["patch", "--no-backup-if-mismatch", "--force", "--silent", "-r", "-"]
        if reverse:   cmdline.append("--reverse")
        if fuzz != 2: cmdline.append("--fuzz=%d" % fuzz)
        cmdline += [result.name, patchfile.name]

        exitcode = subprocess.call(cmdline, stdout=_devnull, stderr=_devnull)
        if exitcode != 0:
            raise PatchApplyError("Failed to apply patch (exitcode %d)." % exitcode)

        # Hack - we can't keep the file open while patching ('patch' might rename/replace
        # the file), so create a new _TemporaryFileWrapper object for the existing path.
        return tempfile._TemporaryFileWrapper(file=open(result.name, 'r+b'), \
                                              name=result.name, delete=True)
    except:
        os.unlink(result.name)
        raise