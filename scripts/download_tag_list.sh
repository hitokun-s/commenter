#!/usr/bin/env bash
file_list="/comment-hackathon/tags/list.txt"
signature="?uid=jgpuauno@gmail.com&Policy=eyJTdGF0ZW1lbnQiOiBbeyJDb25kaXRpb24iOiB7IkRhdGVMZXNzVGhhbiI6IHsiQVdTOkVwb2NoVGltZSI6IDE0NjE5NDIwMDB9fSwgIlJlc291cmNlIjogImh0dHBzOi8vbmljby1vcGVuZGF0YS5qcC9jb21tZW50LWhhY2thdGhvbi8qP3VpZD1qZ3B1YXVub0BnbWFpbC5jb20ifV19&Signature=Wp2CIea~mp80w-20BRCofbxRN2fE2vGzTkENLJJpiavSnK5xZlbiQsXVSmUV1xikcDa0ridduNKoqWGRnpwjmgdC~d4HBvHI5M53yo9PPlKVNxt~G02mOOW4AuJZfncXyYOXp7fz6RE49nn6YBnkwfhd57JUhK9G7qmNYx3I8Ix6VLBATF~o5fnhQusbWhSvT2~gHNf2vkbkvA~UHrYAUFMJppk6hweaOMiO0uDHHoKl2D30dsrowCIHl~IwVgklez~t7UxY7syM5zUcut~OVSTrn2tVkMKNj3P2~XUrZ8ZCT7L26FPg6qfkYIRLmgOtCszAtvPNrCh16f8sCIaEUA__&Key-Pair-Id=APKAINZSYXWBRMHNWVQA"
origin="https://nico-opendata.jp"
 
for line in `wget -q -O - ${origin}${file_list}${signature}`; do
   echo $line
   wget -q -O `basename ${line}` ${origin}${line}${signature}
done