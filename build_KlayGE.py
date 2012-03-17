#!/usr/bin/env python
#-*- coding: ascii -*-

from __future__ import print_function
import os, sys
from blib_util import *

def build_KlayGE(compiler_name, compiler_version, compiler_arch, generator_name):
	curdir = os.path.abspath(os.curdir)

	build_dir = "KlayGE/Build/%s-%d_0-%s" % (compiler_name, compiler_version, compiler_arch)
	if not os.path.exists(build_dir):
		os.makedirs(build_dir)

	os.chdir(build_dir)

	cmake_cmd = batch_command()
	cmake_cmd.add_command('cmake -G "%s" %s' % (generator_name, "../cmake"))
	cmake_cmd.execute()

	config_list = ("Debug", "Release")

	build_cmd = batch_command()
	build_cmd.add_command('CALL "%%VS%d0COMNTOOLS%%..\\..\\VC\\vcvarsall.bat" %s' % (compiler_version, compiler_arch))
	for config in config_list:
		build_cmd.add_command('devenv KlayGE.sln /Build %s /project ALL_BUILD' % config)
		build_cmd.add_command('devenv KlayGE.sln /Build %s /project Install' % config)
	build_cmd.execute()

	os.chdir(curdir)

def build_Samples(compiler_name, compiler_version, compiler_arch, generator_name):
	curdir = os.path.abspath(os.curdir)

	build_dir = "KlayGE/Samples/build/%s-%d_0-%s" % (compiler_name, compiler_version, compiler_arch)
	if not os.path.exists(build_dir):
		os.makedirs(build_dir)

	os.chdir(build_dir)

	cmake_cmd = batch_command()
	cmake_cmd.add_command('cmake -G "%s" %s' % (generator_name, "../cmake"))
	cmake_cmd.execute()

	config_list = ("Debug", "Release")

	build_cmd = batch_command()
	build_cmd.add_command('CALL "%%VS%d0COMNTOOLS%%..\\..\\VC\\vcvarsall.bat" %s' % (compiler_version, compiler_arch))
	for config in config_list:
		build_cmd.add_command('devenv Samples.sln /Build %s /project ALL_BUILD' % config)
		build_cmd.add_command('devenv Samples.sln /Build %s /project Install' % config)
	build_cmd.execute()

	os.chdir(curdir)

def build_Tools(compiler_name, compiler_version, compiler_arch, generator_name):
	curdir = os.path.abspath(os.curdir)

	build_dir = "KlayGE/Tools/build/%s-%d_0-%s" % (compiler_name, compiler_version, compiler_arch)
	if not os.path.exists(build_dir):
		os.makedirs(build_dir)

	os.chdir(build_dir)

	cmake_cmd = batch_command()
	cmake_cmd.add_command('cmake -G "%s" %s' % (generator_name, "../cmake"))
	cmake_cmd.execute()

	config_list = ("Debug", "Release")

	build_cmd = batch_command()
	build_cmd.add_command('CALL "%%VS%d0COMNTOOLS%%..\\..\\VC\\vcvarsall.bat" %s' % (compiler_version, compiler_arch))
	for config in config_list:
		build_cmd.add_command('devenv Tools.sln /Build %s /project ALL_BUILD' % config)
		build_cmd.add_command('devenv Tools.sln /Build %s /project Install' % config)
	build_cmd.execute()

	os.chdir(curdir)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		compiler = sys.argv[1]
	else:
		compiler = ""
	if len(sys.argv) > 2:
		cfg = sys.argv[2]
	else:
		cfg = "x86"

	compiler_info = get_compiler_info(compiler, cfg)

	if 0 == len(compiler_info):
		print("Wrong configuration\n")
		sys.exit(1)

	print("Building KlayGE...")
	for arch in compiler_info[2]:
		build_KlayGE(compiler_info[0], compiler_info[1], arch[0], arch[1])

	print("Building Samples...")
	for arch in compiler_info[2]:
		build_Samples(compiler_info[0], compiler_info[1], arch[0], arch[1])

	print("Building Tools...")
	for arch in compiler_info[2]:
		build_Tools(compiler_info[0], compiler_info[1], arch[0], arch[1])