using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using DownloadArchiver;

namespace Test
{
    [TestClass]
    public class DownloadArchiverTest
    {
        [TestMethod]
        public void Execute()
        {
            var failed = Archive.Execute(fileArchive: "Old", directoryArchive: "Dirs", executableName: "archiveDownload.exe");
            foreach(var f in failed)
            {
                Console.WriteLine(f);
            }
        }
    }
}
