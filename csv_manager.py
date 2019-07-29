import csv


class CSV_Manager:
    def __init__(self, filename):
        self.filename = filename

    def get_csv_as_dicts(self):
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rows = [row for row in csv_reader]
            # print rows
            return self.to_dict(rows)

    def to_dict(self, rows):
        keys = rows[0]
        all_data = {}
        key1 = "arr"
        key2 = "obj"
        all_data[key1] = []
        all_data[key2] = {}

        for row in rows:
            data_dict = {}
            for i in range(0, len(row)):
                data_dict[keys[i]] = row[i]
            all_data[key1].append(data_dict)
        # print all_data
        rows.remove(rows[0])
        for row in rows:
            author = row[3]
            category = row[2]
            if author in all_data[key2]:
                all_data[key2][author].append({keys[0]: row[0], keys[1]: row[1], keys[2]: row[2]})
            else:
                all_data[key2][author] =  [{keys[0]: row[0], keys[1]: row[1], keys[2]: row[2]}]
            if category in all_data[key2]:
                all_data[key2][category].append({keys[0]: row[0], keys[1]: row[1], keys[3]: row[3]})
            else:
                all_data[key2][category] =  [{keys[0]: row[0], keys[1]: row[1], keys[3]: row[3]}]
            
        return all_data

    # def to_dict_2(self, rows):
    #     keys = rows[0]
    #     all_data = {}
    #     # print all_data
    #     return all_data        
