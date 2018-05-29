class table():
    name = ""
    fields = []
    types = []
    current_id = 0
    data ={}
    int_fields={}
    string_fields={}
    def __init__(self, name, fields, types):
        self.name = name
        self.fields = fields
        self.types = types


    def insert(self, fields, values):
        self.data[self.current_id] = row(values)
        self.create_index(self.current_id, fields,values)
        self.current_id = self.current_id + 1

    def create_index(self, idx, fields, values):
        for i in range(len(fields)):
            t = self.types[i]
            f = self.fields[i]
            v = values[i]
            if t == "int":
                if f in self.int_fields:
                    field_map = self.int_fields[f]
                    if v in field_map:
                        field_map[v].append(idx)
                    else:
                        field_map[v] = [idx]
                else:
                    field_map = {}
                    field_map[v] = [idx]
                    self.int_fields[f] = field_map
            if t == "string":
                if f in self.string_fields:
                    field_map = self.string_fields[f]
                    if v in field_map:
                        field_map[v].append(idx)
                    else:
                        field_map[v] = [idx]
                else:
                    field_map = {}
                    field_map[v] = [idx]
                    self.string_fields[f] = field_map


    def select(self, fields, conditions):
        print self.data
        print self.int_fields
        print self.string_fields
        record_ids = self.get_ids(fields, conditions)
        result = []
        print record_ids
        for r in record_ids:
            result.append(self.data[r].get_values(self.get_offset(fields)))
        return result

    def get_ids(self, fields, conditions):
        ids = []
        for c in conditions:
            f = c[0]
            v = c[1]
            if f in self.int_fields:
                ids.extend(self.int_fields[f][v])
            if f in self.string_fields:
                ids.extend(self.string_fields[f][v])
        return ids


    def get_offset(self, fi):
        offset=[]
        for i in range(len(self.fields)):
            for f in fi:
                if self.fields[i] == f:
                    offset.append(i)
        return offset


    def __repr__(self):
        s = self.name
        for i in range(0, len(self.fields)):
            s = s + self.fields[i] + "->" +  self.types[i]
        return s

class row():
    fields = []
    def __init__(self, f):
        self.fields = f

    def get_values(self, fields_off):
        row = []
        for f in fields_off:
            row.append(self.fields[f])
        return row

    def __repr__(self):
        return str(self.fields)



class database():
    tables = {}
    def create_table(self, table_name, fields, types):
        t = table(table_name, fields, types)
        self.tables[table_name]=t

    def insert_table(self, name, fields, values):
        self.tables[name].insert(fields, values)

    def select(self, name, fields, conditions):
        return self.tables[name].select(fields, conditions)

def main():
    d = database()
    d.create_table("user", ["userid","username","email"], ["int","string","string"])
    d.insert_table("user", ["userid","username","email"], ["123","sandeep","yahoo"])

    d.insert_table("user", ["userid","username","email"], ["124","sandeep","gg"])
    d.insert_table("user", ["userid","username","email"], ["125","sanep","ydo"])
    d.insert_table("user", ["userid","username","email"], ["126","san","yahdo"])
    d.insert_table("user", ["userid","username","email"], ["127","sandeep","gmail"])

    print d.select("user", ["userid","email"], [["username", "sandeep"]])
main()
