using Syroot.Windows.IO;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DownloadArchiver
{
    public static class Archive
    {
        public static IEnumerable<string> Execute(string fileArchive, string directoryArchive, string executableName)
        {
            var failed = new List<string>();
            var downloadFolder = new KnownFolder(KnownFolderType.Downloads);
            var downloads = downloadFolder.Path;

            //Move old directory to a new old directory

            var old = Path.Combine(downloads, fileArchive);
            var dir = Path.Combine(downloads, directoryArchive);
            if (Directory.Exists(old))
            {
                CreateNestedOld(fileArchive, downloads, old);
            }
            else
            {
                Directory.CreateDirectory(old);
            }

            if (!Directory.Exists(dir))
            {
                Directory.CreateDirectory(dir);
            }

            failed.AddRange(ArchiveDirectories(fileArchive, directoryArchive, downloads, dir));

            failed.AddRange(ArchiveFiles(executableName, downloads, old));

            return failed;
        }

        private static void CreateNestedOld(string fileArchive, string downloads, string old)
        {
            var tmp = Path.Combine(downloads, fileArchive + ".tmp.archive");
            Directory.Move(old, tmp);
            Directory.CreateDirectory(old);
            Directory.Move(tmp, Path.Combine(old, fileArchive));
        }

        private static IEnumerable<string> ArchiveDirectories(string fileArchive, string directoryArchive, string downloads, string dir)
        {
            foreach (var d in Directory.EnumerateDirectories(downloads).Where(d =>
                     Path.GetFileName(d) != fileArchive &&
                     Path.GetFileName(d) != directoryArchive))
            {
                var destination = Path.Combine(dir, Path.GetFileName(d));
                string failed = null;
                try
                {
                    Directory.Move(d, destination);
                }
                catch (IOException)
                {
                    failed = $"move '{d}' '{destination}'";
                }

                if (failed != null)
                    yield return failed;
            }
        }

        private static IEnumerable<string> ArchiveFiles(string executableName, string downloads, string old)
        {
            foreach (var f in Directory.EnumerateFiles(downloads).Where(f =>
                     Path.GetFileName(f) != executableName)) //In case the executable ends up being stored here
            {
                var destination = Path.Combine(old, Path.GetFileName(f));
                string failed = null;
                try
                {
                    File.Move(f, destination);
                }
                catch (IOException)
                {
                    failed = $"move '{f}' '{destination}'";
                }

                if (failed != null)
                    yield return failed;
            }
        }
    }
}
