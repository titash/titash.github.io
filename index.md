I have been working on the following projects:

- **File Sorter** is a Python script that organizes files in a folder based on their extensions. It creates subfolders for each unique extension and moves the corresponding files into their respective subfolders([repo](https://github.com/titash/file_sorter))

         +-----------------+
         |     Sorter      |
         +-----------------+
                  |
                  |   +-------------------+
                  +-->|  File Directory   |
                      +-------------------+
                               |
                     +---------+---------+
                     |                   |
         +-----------+---+       +-------+-----+
         |  .txt Files   |       |  .jpg Files |
         +---------------+       +-------------+
               |                           |
               |                           |
          +----+----+              +-------+-----+
          |  File1  |              |  File3  |
          +---------+              +---------+
               |
          +----+----+
          |  File2  |
          +---------+
               |
          +----+----+
          |  File4  |
          +---------+
               |
          +----+----+
          |  File5  |
          +---------+

